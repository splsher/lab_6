"""first commit 2021-11

Revision ID: 1be43298dab7
Revises: 
Create Date: 2021-11-21 14:51:14.359904

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = '1be43298dab7'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('account',
    sa.Column('ownerid', sa.Integer(), nullable=False),
    sa.Column('balance', sa.Integer(), nullable=True),
    sa.PrimaryKeyConstraint('ownerid')
    )
    op.create_table('family',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('name', sa.String(length=45), nullable=True),
    sa.Column('account_ownerId', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['account_ownerId'], ['account.ownerid'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('users',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('username', sa.String(length=45), nullable=True),
    sa.Column('firstname', sa.String(length=45), nullable=True),
    sa.Column('lastname', sa.String(length=45), nullable=True),
    sa.Column('email', sa.String(length=45), nullable=True),
    sa.Column('password', sa.String(length=45), nullable=True),
    sa.Column('phone', sa.String(length=45), nullable=True),
    sa.Column('family_id', sa.Integer(), nullable=False),
    sa.ForeignKeyConstraint(['family_id'], ['family.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('budget_note',
    sa.Column('id', sa.Integer(), autoincrement=True, nullable=False),
    sa.Column('sum', sa.Integer(), nullable=True),
    sa.Column('date', sa.Date(), nullable=True),
    sa.Column('type', sa.String(length=40), nullable=True),
    sa.Column('users_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['users_id'], ['users.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('budget_note')
    op.drop_table('users')
    op.drop_table('family')
    op.drop_table('account')
    # ### end Alembic commands ###
