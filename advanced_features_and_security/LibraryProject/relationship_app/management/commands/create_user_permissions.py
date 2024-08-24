# You can run this in a management command or in a migration

from django.contrib.auth.models import User, Group, Permission
from django.contrib.contenttypes.models import ContentType
from relationship_app.models import Book

def assign_permissions():
    # Get the content type for the Book model
    book_content_type = ContentType.objects.get_for_model(Book)

    # Get the permissions
    add_permission = Permission.objects.get(content_type=book_content_type, codename='can_add_book')
    change_permission = Permission.objects.get(content_type=book_content_type, codename='can_change_book')
    delete_permission = Permission.objects.get(content_type=book_content_type, codename='can_delete_book')

    # Create groups (if they don't exist)
    librarian_group, _ = Group.objects.get_or_create(name='Librarian')
    admin_group, _ = Group.objects.get_or_create(name='Admin')

    # Assign permissions to groups
    librarian_group.permissions.add(add_permission, change_permission)
    admin_group.permissions.add(add_permission, change_permission, delete_permission)

    # Assign users to groups (example)
    librarian_user = User.objects.get(username='librarian_username')
    admin_user = User.objects.get(username='admin_username')

    librarian_user.groups.add(librarian_group)
    admin_user.groups.add(admin_group)

# Call this function when you want to assign permissions
assign_permissions()