"""
Research Proposal Tool
A tool for processing research papers and generating structured research proposals.
"""

__version__ = "1.0.0"
__author__ = "Research Proposal Tool"

from .paper_processor import PaperProcessor
from .paper_summarizer import PaperSummarizer
from .reference_organizer import ReferenceOrganizer
from .proposal_generator import ProposalGenerator

__all__ = [
    'PaperProcessor',
    'PaperSummarizer',
    'ReferenceOrganizer',
    'ProposalGenerator'
]
