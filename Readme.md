# College Management System Database Migrations

## Overview
This directory contains database migrations for the College Management System.

## Migration Commands
- Initialize migrations:
```bash
flask db init
```

- Create new migration:
```bash
flask db migrate -m "description"
```

- Apply migrations:
```bash
flask db upgrade
```

- Rollback migrations:
```bash
flask db downgrade
```

- View migration history:
```bash
flask db history
```

## Directory Structure
```
migrations/
├── README.md
├── alembic.ini
├── env.py
├── script.py.mako
└── versions/
```

## Migration Naming Convention
- Format: `YYYYMMDD_HHMMSS_description.py`
- Example: `20241123_100000_create_users_table.py`

## Best Practices
1. Always test both `upgrade()` and `downgrade()` functions
2. Create atomic migrations (one logical change per migration)
3. Never modify existing migrations after they're committed
4. Include clear descriptions in migration messages
5. Always backup database before running migrations in production

## Common Issues
1. If migrations fail, check:
   - Database connection
   - Model imports
   - Existing table conflicts
   - Permission issues

2. For rollback issues:
   - Ensure downgrade functions are properly implemented
   - Check for dependency conflicts
   - Verify database state