"""Removing phone_number column

Revision ID: dd770b4b97f9
Revises: fd492f3856d3
Create Date: 2024-06-20 11:40:33.827712

"""
from typing import Sequence, Union

from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision: str = 'dd770b4b97f9'
down_revision: Union[str, None] = 'fd492f3856d3'
branch_labels: Union[str, Sequence[str], None] = None
depends_on: Union[str, Sequence[str], None] = None


def upgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.alter_column('heros', 'joined_on',
               existing_type=sa.TIMESTAMP(),
               type_=sa.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('users', 'created_at',
               existing_type=sa.TIMESTAMP(),
               type_=sa.TIMESTAMP(timezone=True),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    if op.get_context().dialect.name == 'postgresql':
        # PostgreSQL example (using a different name than uq_phone_number)
        op.execute('ALTER TABLE users DROP CONSTRAINT IF EXISTS uq_phone_number CASCADE')
        op.execute('DROP INDEX IF EXISTS uq_phone_number')

    # Drop the column
    op.drop_column('users', 'phone_number')
    # ### end Alembic commands ###


def downgrade() -> None:
    # ### commands auto generated by Alembic - please adjust! ###
    op.add_column('users', sa.Column('phone_number', sa.INTEGER(), autoincrement=False, nullable=True))
    op.create_index('uq_phone_number', 'users', [sa.text('phone_number NULLS FIRST')], unique=True, postgresql_using='prefix')
    op.create_unique_constraint('uq_phone_number', 'users', ['phone_number'])
    op.alter_column('users', 'created_at',
               existing_type=sa.TIMESTAMP(timezone=True),
               type_=sa.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    op.alter_column('heros', 'joined_on',
               existing_type=sa.TIMESTAMP(timezone=True),
               type_=sa.TIMESTAMP(),
               existing_nullable=False,
               existing_server_default=sa.text('now()'))
    # ### end Alembic commands ###
