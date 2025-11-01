"""
Paper Processor Module
Extracts key information from research papers including abstracts, methods, and findings.
"""

import re
from typing import Dict, List, Optional


class PaperProcessor:
    """Process research papers to extract key information."""
    
    def __init__(self):
        """Initialize the paper processor."""
        self.section_patterns = {
            'abstract': [
                r'(?i)^abstract\s*$',
                r'(?i)^abstract\s*:',
                r'(?i)^1\.\s*abstract',
            ],
            'introduction': [
                r'(?i)^introduction\s*$',
                r'(?i)^1\.\s*introduction',
            ],
            'methods': [
                r'(?i)^methods?\s*$',
                r'(?i)^methodology\s*$',
                r'(?i)^materials?\s+and\s+methods?',
                r'(?i)^\d+\.\s*methods?',
                r'(?i)^\d+\.\s*methodology',
            ],
            'results': [
                r'(?i)^results?\s*$',
                r'(?i)^findings?\s*$',
                r'(?i)^\d+\.\s*results?',
                r'(?i)^\d+\.\s*findings?',
            ],
            'discussion': [
                r'(?i)^discussion\s*$',
                r'(?i)^\d+\.\s*discussion',
            ],
            'conclusion': [
                r'(?i)^conclusions?\s*$',
                r'(?i)^\d+\.\s*conclusions?',
            ]
        }
    
    def extract_metadata(self, paper_text: str) -> Dict[str, str]:
        """
        Extract metadata from paper text.
        
        Args:
            paper_text: Full text of the research paper
            
        Returns:
            Dictionary containing title, authors, and other metadata
        """
        lines = paper_text.strip().split('\n')
        metadata = {
            'title': '',
            'authors': '',
            'year': '',
            'keywords': []
        }
        
        # Extract title (usually first non-empty line)
        for line in lines[:10]:
            if line.strip() and len(line.strip()) > 10:
                metadata['title'] = line.strip()
                break
        
        # Look for year pattern
        year_pattern = r'\b(19|20)\d{2}\b'
        year_matches = re.findall(year_pattern, paper_text[:1000])
        if year_matches:
            metadata['year'] = year_matches[0]
        
        # Look for keywords section
        keywords_pattern = r'(?i)keywords?\s*:?\s*(.+?)(?:\n\n|\n[A-Z]|$)'
        keywords_match = re.search(keywords_pattern, paper_text[:2000])
        if keywords_match:
            keywords_text = keywords_match.group(1)
            metadata['keywords'] = [k.strip() for k in re.split(r'[;,]', keywords_text) if k.strip()]
        
        return metadata
    
    def extract_section(self, paper_text: str, section_name: str) -> str:
        """
        Extract a specific section from the paper.
        
        Args:
            paper_text: Full text of the research paper
            section_name: Name of the section to extract (e.g., 'abstract', 'methods')
            
        Returns:
            Text content of the section
        """
        if section_name not in self.section_patterns:
            return ""
        
        lines = paper_text.split('\n')
        section_start = None
        section_end = None
        
        # Find section start
        for i, line in enumerate(lines):
            for pattern in self.section_patterns[section_name]:
                if re.match(pattern, line.strip()):
                    section_start = i + 1
                    break
            if section_start:
                break
        
        if section_start is None:
            return ""
        
        # Find section end (next section header or end of document)
        for i in range(section_start, len(lines)):
            line = lines[i].strip()
            # Check if this line starts a new section
            for other_section, patterns in self.section_patterns.items():
                if other_section != section_name:
                    for pattern in patterns:
                        if re.match(pattern, line):
                            section_end = i
                            break
                    if section_end:
                        break
            if section_end:
                break
        
        if section_end is None:
            section_end = min(section_start + 100, len(lines))  # Limit to 100 lines
        
        section_text = '\n'.join(lines[section_start:section_end])
        return section_text.strip()
    
    def extract_abstract(self, paper_text: str) -> str:
        """Extract the abstract from a research paper."""
        return self.extract_section(paper_text, 'abstract')
    
    def extract_methods(self, paper_text: str) -> str:
        """Extract the methods/methodology section from a research paper."""
        return self.extract_section(paper_text, 'methods')
    
    def extract_results(self, paper_text: str) -> str:
        """Extract the results/findings section from a research paper."""
        return self.extract_section(paper_text, 'results')
    
    def extract_conclusion(self, paper_text: str) -> str:
        """Extract the conclusion section from a research paper."""
        return self.extract_section(paper_text, 'conclusion')
    
    def process_paper(self, paper_text: str) -> Dict[str, any]:
        """
        Process a complete research paper and extract all key information.
        
        Args:
            paper_text: Full text of the research paper
            
        Returns:
            Dictionary containing all extracted information
        """
        return {
            'metadata': self.extract_metadata(paper_text),
            'abstract': self.extract_abstract(paper_text),
            'methods': self.extract_methods(paper_text),
            'results': self.extract_results(paper_text),
            'conclusion': self.extract_conclusion(paper_text)
        }
