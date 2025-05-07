import os
import django
from django.core.wsgi import get_wsgi_application

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'PI_DOT.settings')  # Replace 'your_project_name'

django.setup()
application = get_wsgi_application()

def handler(event, context):
    # Adapt the WSGI application to Vercel's event format
    # This is a simplified example and might need adjustments based on your needs.
    # For more complex scenarios, consider using libraries like 'serverless-wsgi'.
    from io import BytesIO
    from django.core.handlers.wsgi import WSGIRequest

    raw_body = event.get('body', '')
    if event.get('isBase64Encoded', False):
        import base64
        body = BytesIO(base64.b64decode(raw_body))
    else:
        body = BytesIO(raw_body.encode('utf-8'))

    environ = {
        'REQUEST_METHOD': event.get('httpMethod', 'GET'),
        'PATH_INFO': event.get('path', '/'),
        'QUERY_STRING': event.get('queryStringParameters', {}).get('q', ''), # Adjust as needed
        'SERVER_NAME': 'vercel.com',
        'SERVER_PORT': '443',
        'wsgi.version': (1, 0),
        'wsgi.url_scheme': 'https',
        'wsgi.input': body,
        'wsgi.errors': sys.stderr,
        'wsgi.multithread': False,
        'wsgi.multiprocess': False,
        'wsgi.run_once': True,
        'REMOTE_ADDR': event.get('headers', {}).get('x-forwarded-for', '127.0.0.1').split(',')[0],
        'HTTP_HOST': event.get('headers', {}).get('host', 'vercel.com'),
        **{f'HTTP_{key.upper().replace("-", "_")}': value
           for key, value in event.get('headers', {}).items() if key.lower() not in ('host', 'x-forwarded-for')},
    }

    request = WSGIRequest(environ)
    response = application(environ, lambda status, headers: None) # We'll handle the response differently

    status_line = f"HTTP/1.1 {response.status_code} {response.reason_phrase}"
    response_headers = list(response.items())
    response_body = b''.join(response)

    return {
        "statusCode": response.status_code,
        "headers": dict(response_headers),
        "body": response_body.decode('utf-8', errors='ignore') if isinstance(response_body, bytes) else response_body,
        "isBase64Encoded": False
    }

if __name__ == "__main__":
    # This is for local testing (optional)
    import json
    class MockEvent:
        def get(self, key, default=None):
            if key == 'httpMethod':
                return 'GET'
            elif key == 'path':
                return '/'
            elif key == 'queryStringParameters':
                return {'q': 'test'}
            elif key == 'headers':
                return {'Host': 'localhost'}
            return default

    class MockContext:
        pass

    result = handler(MockEvent(), MockContext())
    print(json.dumps(result, indent=2))

import sys