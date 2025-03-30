"""
Common message constants used throughout the application.
"""

# HTTP Status Messages
HTTP_200_OK = "Success"
HTTP_201_CREATED = "Resource created successfully"
HTTP_400_BAD_REQUEST = "Bad request"
HTTP_401_UNAUTHORIZED = "Unauthorized"
HTTP_403_FORBIDDEN = "Forbidden"
HTTP_404_NOT_FOUND = "Resource not found"
HTTP_500_INTERNAL_SERVER_ERROR = "Internal server error"

# Database Messages
DB_CONNECTION_ERROR = "Database connection error"
DB_QUERY_ERROR = "Database query error"
DB_CREATE_ERROR = "Error creating database resource"
DB_UPDATE_ERROR = "Error updating database resource"
DB_DELETE_ERROR = "Error deleting database resource"

# Authentication Messages
AUTH_INVALID_CREDENTIALS = "Invalid credentials"
AUTH_TOKEN_EXPIRED = "Authentication token has expired"
AUTH_TOKEN_INVALID = "Invalid authentication token"
AUTH_USER_NOT_FOUND = "User not found"

# Validation Messages
VALIDATION_ERROR = "Validation error"
REQUIRED_FIELD = "This field is required"
INVALID_FORMAT = "Invalid format"
INVALID_VALUE = "Invalid value"

# Server Messages
SERVER_STARTUP = "Server is starting up"
SERVER_SHUTDOWN = "Server is shutting down"
SERVER_RUNNING = "Server is running"
SERVER_ERROR = "Server error occurred"

# Resource Messages
RESOURCE_CREATED = "Resource created successfully"
RESOURCE_UPDATED = "Resource updated successfully"
RESOURCE_DELETED = "Resource deleted successfully"
RESOURCE_NOT_FOUND = "Resource not found"
RESOURCE_ALREADY_EXISTS = "Resource already exists"

# API Messages
API_RATE_LIMIT = "Rate limit exceeded"
API_INVALID_REQUEST = "Invalid request"
API_SUCCESS = "Operation completed successfully"
API_ERROR = "Operation failed"

# File Messages
FILE_UPLOAD_SUCCESS = "File uploaded successfully"
FILE_UPLOAD_ERROR = "Error uploading file"
FILE_NOT_FOUND = "File not found"
FILE_DELETE_SUCCESS = "File deleted successfully"
FILE_DELETE_ERROR = "Error deleting file" 