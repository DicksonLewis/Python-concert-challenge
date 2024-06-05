from alembic import op
import sqlalchemy as sa

# revision identifiers, used by Alembic.
revision = '<unique_id>'
down_revision = 'b01979c7ce45'
branch_labels = None
depends_on = None

def upgrade():
    op.create_table('concerts',
        sa.Column('id', sa.Integer(), primary_key=True),
        sa.Column('band_id', sa.Integer(), sa.ForeignKey('bands.id')),
        sa.Column('venue_id', sa.Integer(), sa.ForeignKey('venues.id')),
        sa.Column('date', sa.String())
    )

def downgrade():
    op.drop_table('concerts')
