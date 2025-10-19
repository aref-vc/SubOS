#!/usr/bin/env python3
"""
SubOS Backend Entry Point
Run the Flask development server
"""
import os
from app import create_app

# Determine environment
env = os.getenv('FLASK_ENV', 'development')

# Create app
app = create_app(env)

if __name__ == '__main__':
    port = app.config.get('PORT', 3038)
    debug = app.config.get('DEBUG', True)

    print(f"""
    ╔═══════════════════════════════════════════╗
    ║                                           ║
    ║           SubOS Backend API               ║
    ║                                           ║
    ╚═══════════════════════════════════════════╝

    🚀 Server starting on http://localhost:{port}
    📚 API Docs: http://localhost:{port}/api/v1/status
    💚 Health check: http://localhost:{port}/health

    Environment: {env}
    Debug mode: {debug}

    Press CTRL+C to quit
    """)

    app.run(
        host='0.0.0.0',
        port=port,
        debug=debug
    )
