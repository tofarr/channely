# Channely Database Entities

This package contains SQLAlchemy entity definitions that correspond to the dataclasses defined in the `channely.model` package.

## Overview

The database entities are organized as follows:

### Base Classes
- `Base`: The declarative base for all SQLAlchemy entities
- `BaseEntity`: Base entity with common fields (id, created_at, updated_at)
- `BaseEntityWithoutTimestamps`: Base entity with only id field

### Main Entities
- `UserEntity`: User accounts and profiles
- `ChannelEntity`: Communication channels
- `ContentEntity`: Content/messages within channels
- `AttachmentEntity`: File attachments to content
- `ContentWebhookEntity`: Webhook configurations for content events
- `ContentWebhookHeaderEntity`: HTTP headers for webhooks

### Permission Entities
- `ChannelPermissionEntity`: Channel-level permissions
- `ContentPermissionEntity`: Content-level permissions  
- `SystemPermissionEntity`: System-wide permissions

### Enums
All enum types from the model package are re-exported for database use:
- `UserStatus`, `ChannelStatus`, `ContentStatus`
- `ChannelPermissionType`, `ContentPermissionType`, `SystemPermissionType`
- `ContentEventType`

## Usage

```python
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from channely.database import Base, UserEntity, ChannelEntity

# Create database engine
engine = create_engine("postgresql://user:pass@localhost/channely")

# Create all tables
Base.metadata.create_all(engine)

# Create session
Session = sessionmaker(bind=engine)
session = Session()

# Create entities
user = UserEntity(username="john_doe", display_name="John Doe")
session.add(user)
session.commit()
```

## Example

See `example.py` for a complete working example using an in-memory SQLite database.

## Relationships

The entities include proper SQLAlchemy relationships:
- Users can create channels and content
- Channels can contain content and have permissions
- Content can have attachments and permissions
- Webhooks can have custom headers
- All permission entities link to users and their respective resources

## Database Support

The entities are designed to work with PostgreSQL (using UUID primary keys) but can also work with SQLite for development and testing.