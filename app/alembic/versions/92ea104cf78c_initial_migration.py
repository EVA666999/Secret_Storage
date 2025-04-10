"""Initial migration

Revision ID: 92ea104cf78c
Revises: 5a02f346b304
Create Date: 2025-04-06 04:14:17.851925

"""

from typing import Sequence, Union

import sqlalchemy as sa

from alembic import op

# revision identifiers, used by Alembic.
revision: str = "92ea104cf78c"
down_revision: Union[str, None] = "5a02f346b304"
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    """Upgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table(
        "secret_logs",
        sa.Column(
            "id",
            sa.Integer(),
            nullable=False,
            comment="Уникальный идентификатор записи лога",
        ),
        sa.Column(
            "secret_id", sa.Integer(), nullable=False, comment="ID созданного секрета"
        ),
        sa.Column(
            "action",
            sa.String(length=50),
            nullable=False,
            comment="Тип действия (создание, чтение, удаление)",
        ),
        sa.Column(
            "ip_address",
            sa.String(length=50),
            nullable=True,
            comment="IP-адрес клиента",
        ),
        sa.Column(
            "user_agent",
            sa.String(length=255),
            nullable=True,
            comment="User-Agent клиента",
        ),
        sa.Column(
            "ttl_seconds",
            sa.Integer(),
            nullable=True,
            comment="Время жизни секрета в секундах",
        ),
        sa.Column(
            "timestamp",
            sa.DateTime(timezone=True),
            server_default=sa.text("now()"),
            nullable=False,
            comment="Время выполнения действия",
        ),
        sa.Column(
            "additional_info",
            sa.Text(),
            nullable=True,
            comment="Дополнительная информация",
        ),
        sa.PrimaryKeyConstraint("id"),
    )
    op.create_index(op.f("ix_secret_logs_id"), "secret_logs", ["id"], unique=False)
    # ### end Alembic commands ###


def downgrade() -> None:
    """Downgrade schema."""
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_index(op.f("ix_secret_logs_id"), table_name="secret_logs")
    op.drop_table("secret_logs")
    # ### end Alembic commands ###
