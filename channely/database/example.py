"""
Example usage of the database entities.

This script demonstrates how to create an in-memory SQLite database
and work with the entities.
"""

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from channely.database import (
    Base,
    UserEntity,
    ChannelEntity,
    ContentEntity,
    UserStatus,
    ChannelStatus,
    ContentStatus,
)


def create_example_data():
    """Create example data in an in-memory SQLite database."""

    # Create an in-memory SQLite database
    engine = create_engine("sqlite:///:memory:", echo=True)

    # Create all tables
    Base.metadata.create_all(engine)

    # Create a session
    Session = sessionmaker(bind=engine)
    session = Session()

    try:
        # Create a user
        user = UserEntity(
            username="john_doe",
            display_name="John Doe",
            status=UserStatus.ACTIVE,
            locale="en_US",
            theme="dark",
        )
        session.add(user)
        session.flush()  # Get the ID

        # Create a channel
        channel = ChannelEntity(
            status=ChannelStatus.ACTIVE, theme="blue", creator_id=user.id
        )
        session.add(channel)
        session.flush()  # Get the ID

        # Create content in the channel
        content = ContentEntity(
            channel_id=channel.id,
            text="Hello, world!",
            markdown="# Hello, world!\n\nThis is my first post.",
            status=ContentStatus.ACTIVE,
            creator=user.id,
        )
        session.add(content)

        # Commit the transaction
        session.commit()

        # Query the data
        print("Users:")
        for u in session.query(UserEntity).all():
            print(f"  - {u.username} ({u.display_name})")

        print("\nChannels:")
        for c in session.query(ChannelEntity).all():
            print(
                f"  - Channel {c.id} created by {c.creator.username if c.creator else 'unknown'}"
            )

        print("\nContent:")
        for content in session.query(ContentEntity).all():
            print(f"  - '{content.text}' in channel {content.channel_id}")

    finally:
        session.close()


if __name__ == "__main__":
    create_example_data()
