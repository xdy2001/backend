"""empty message

Revision ID: a24b7d71e3ba
Revises: 
Create Date: 2018-06-23 08:09:38.926134

"""
from alembic import op
import sqlalchemy as sa


# revision identifiers, used by Alembic.
revision = 'a24b7d71e3ba'
down_revision = None
branch_labels = None
depends_on = None


def upgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.create_table('roles',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('name', sa.String(length=64), nullable=True),
    sa.PrimaryKeyConstraint('id'),
    sa.UniqueConstraint('name')
    )
    op.create_table('wenbai_readers',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('token', sa.String(length=64), nullable=True),
    sa.Column('name', sa.Unicode(length=64), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wenbai_readers_name'), 'wenbai_readers', ['name'], unique=False)
    op.create_index(op.f('ix_wenbai_readers_token'), 'wenbai_readers', ['token'], unique=True)
    op.create_table('wenbai_scriptures',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scripture_display', sa.Unicode(length=16), nullable=True),
    sa.Column('scripture_title', sa.Unicode(length=128), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wenbai_scriptures_scripture_display'), 'wenbai_scriptures', ['scripture_display'], unique=False)
    op.create_index(op.f('ix_wenbai_scriptures_scripture_title'), 'wenbai_scriptures', ['scripture_title'], unique=False)
    op.create_table('users',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('username', sa.String(length=64), nullable=True),
    sa.Column('role_id', sa.Integer(), nullable=True),
    sa.ForeignKeyConstraint(['role_id'], ['roles.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_users_username'), 'users', ['username'], unique=True)
    op.create_table('wenbai_chapters',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('scripture_id', sa.Integer(), nullable=True),
    sa.Column('chapter_display', sa.Unicode(length=16), nullable=True),
    sa.Column('chapter__title', sa.Unicode(length=128), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['scripture_id'], ['wenbai_scriptures.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wenbai_chapters_chapter__title'), 'wenbai_chapters', ['chapter__title'], unique=False)
    op.create_index(op.f('ix_wenbai_chapters_chapter_display'), 'wenbai_chapters', ['chapter_display'], unique=False)
    op.create_table('wenbai_sections',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('section_display', sa.Unicode(length=16), nullable=True),
    sa.Column('section__title', sa.Unicode(length=128), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['wenbai_chapters.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_index(op.f('ix_wenbai_sections_section__title'), 'wenbai_sections', ['section__title'], unique=False)
    op.create_index(op.f('ix_wenbai_sections_section_display'), 'wenbai_sections', ['section_display'], unique=False)
    op.create_table('wenbai_sentences',
    sa.Column('id', sa.BigInteger(), nullable=False),
    sa.Column('scripture_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('section_id', sa.Integer(), nullable=True),
    sa.Column('classic_text', sa.Text(), nullable=True),
    sa.Column('modern_text', sa.Text(), nullable=True),
    sa.Column('annotation_text', sa.Text(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['wenbai_chapters.id'], ),
    sa.ForeignKeyConstraint(['scripture_id'], ['wenbai_scriptures.id'], ),
    sa.ForeignKeyConstraint(['section_id'], ['wenbai_sections.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    op.create_table('wenbai_recent_list',
    sa.Column('id', sa.Integer(), nullable=False),
    sa.Column('reader_id', sa.Integer(), nullable=True),
    sa.Column('scripture_id', sa.Integer(), nullable=True),
    sa.Column('chapter_id', sa.Integer(), nullable=True),
    sa.Column('section_id', sa.Integer(), nullable=True),
    sa.Column('sentence_id', sa.BigInteger(), nullable=True),
    sa.Column('updated_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP ON UPDATE CURRENT_TIMESTAMP'), nullable=True),
    sa.Column('created_at', sa.TIMESTAMP(), server_default=sa.text(u'CURRENT_TIMESTAMP'), nullable=True),
    sa.ForeignKeyConstraint(['chapter_id'], ['wenbai_chapters.id'], ),
    sa.ForeignKeyConstraint(['reader_id'], ['wenbai_readers.id'], ),
    sa.ForeignKeyConstraint(['scripture_id'], ['wenbai_scriptures.id'], ),
    sa.ForeignKeyConstraint(['section_id'], ['wenbai_sections.id'], ),
    sa.ForeignKeyConstraint(['sentence_id'], ['wenbai_sentences.id'], ),
    sa.PrimaryKeyConstraint('id')
    )
    # ### end Alembic commands ###


def downgrade():
    # ### commands auto generated by Alembic - please adjust! ###
    op.drop_table('wenbai_recent_list')
    op.drop_table('wenbai_sentences')
    op.drop_index(op.f('ix_wenbai_sections_section_display'), table_name='wenbai_sections')
    op.drop_index(op.f('ix_wenbai_sections_section__title'), table_name='wenbai_sections')
    op.drop_table('wenbai_sections')
    op.drop_index(op.f('ix_wenbai_chapters_chapter_display'), table_name='wenbai_chapters')
    op.drop_index(op.f('ix_wenbai_chapters_chapter__title'), table_name='wenbai_chapters')
    op.drop_table('wenbai_chapters')
    op.drop_index(op.f('ix_users_username'), table_name='users')
    op.drop_table('users')
    op.drop_index(op.f('ix_wenbai_scriptures_scripture_title'), table_name='wenbai_scriptures')
    op.drop_index(op.f('ix_wenbai_scriptures_scripture_display'), table_name='wenbai_scriptures')
    op.drop_table('wenbai_scriptures')
    op.drop_index(op.f('ix_wenbai_readers_token'), table_name='wenbai_readers')
    op.drop_index(op.f('ix_wenbai_readers_name'), table_name='wenbai_readers')
    op.drop_table('wenbai_readers')
    op.drop_table('roles')
    # ### end Alembic commands ###
