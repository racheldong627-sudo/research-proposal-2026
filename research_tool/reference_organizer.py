"""
Reference Organizer Module
Manages and organizes research paper references.
"""

from typing import Dict, List, Optional
import json


class ReferenceOrganizer:
    """Organize and manage research paper references."""
    
    def __init__(self):
        """Initialize the reference organizer."""
        self.references = []
    
    def add_reference(self, title: str, authors: str = "", year: str = "", 
                     source: str = "", doi: str = "", notes: str = "") -> int:
        """
        Add a new reference to the collection.
        
        Args:
            title: Title of the paper
            authors: Authors of the paper
            year: Publication year
            source: Journal/conference name
            doi: DOI or URL
            notes: Additional notes
            
        Returns:
            Index of the added reference
        """
        reference = {
            'id': len(self.references) + 1,
            'title': title,
            'authors': authors,
            'year': year,
            'source': source,
            'doi': doi,
            'notes': notes
        }
        self.references.append(reference)
        return reference['id']
    
    def add_reference_from_paper_data(self, paper_data: Dict) -> int:
        """
        Add a reference from processed paper data.
        
        Args:
            paper_data: Dictionary containing paper information (from PaperProcessor)
            
        Returns:
            Index of the added reference
        """
        metadata = paper_data.get('metadata', {})
        return self.add_reference(
            title=metadata.get('title', 'Unknown'),
            authors=metadata.get('authors', ''),
            year=metadata.get('year', ''),
            notes=f"Keywords: {', '.join(metadata.get('keywords', []))}"
        )
    
    def get_reference(self, ref_id: int) -> Optional[Dict]:
        """
        Get a reference by ID.
        
        Args:
            ref_id: Reference ID
            
        Returns:
            Reference dictionary or None if not found
        """
        for ref in self.references:
            if ref['id'] == ref_id:
                return ref
        return None
    
    def list_references(self, sort_by: str = 'id') -> List[Dict]:
        """
        List all references.
        
        Args:
            sort_by: Field to sort by ('id', 'year', 'title', 'authors')
            
        Returns:
            List of all references
        """
        if sort_by == 'year':
            return sorted(self.references, key=lambda x: x.get('year', ''), reverse=True)
        elif sort_by == 'title':
            return sorted(self.references, key=lambda x: x.get('title', '').lower())
        elif sort_by == 'authors':
            return sorted(self.references, key=lambda x: x.get('authors', '').lower())
        else:
            return self.references.copy()
    
    def search_references(self, query: str) -> List[Dict]:
        """
        Search references by keyword.
        
        Args:
            query: Search query
            
        Returns:
            List of matching references
        """
        query_lower = query.lower()
        results = []
        
        for ref in self.references:
            searchable_text = f"{ref.get('title', '')} {ref.get('authors', '')} {ref.get('notes', '')}".lower()
            if query_lower in searchable_text:
                results.append(ref)
        
        return results
    
    def format_reference_apa(self, ref: Dict) -> str:
        """
        Format a reference in APA style.
        
        Args:
            ref: Reference dictionary
            
        Returns:
            APA-formatted reference string
        """
        parts = []
        
        if ref.get('authors'):
            parts.append(f"{ref['authors']}.")
        
        if ref.get('year'):
            parts.append(f"({ref['year']}).")
        
        if ref.get('title'):
            parts.append(f"{ref['title']}.")
        
        if ref.get('source'):
            parts.append(f"{ref['source']}.")
        
        if ref.get('doi'):
            parts.append(f"DOI: {ref['doi']}")
        
        return ' '.join(parts)
    
    def format_reference_ieee(self, ref: Dict, ref_number: int) -> str:
        """
        Format a reference in IEEE style.
        
        Args:
            ref: Reference dictionary
            ref_number: Reference number
            
        Returns:
            IEEE-formatted reference string
        """
        parts = [f"[{ref_number}]"]
        
        if ref.get('authors'):
            parts.append(f"{ref['authors']},")
        
        if ref.get('title'):
            parts.append(f'"{ref["title"]},"')
        
        if ref.get('source'):
            parts.append(f"{ref['source']},")
        
        if ref.get('year'):
            parts.append(f"{ref['year']}.")
        
        return ' '.join(parts)
    
    def export_references(self, format: str = 'apa') -> str:
        """
        Export all references in specified format.
        
        Args:
            format: Citation format ('apa' or 'ieee')
            
        Returns:
            Formatted references as string
        """
        lines = []
        
        for i, ref in enumerate(self.references, 1):
            if format == 'ieee':
                lines.append(self.format_reference_ieee(ref, i))
            else:  # Default to APA
                lines.append(self.format_reference_apa(ref))
        
        return '\n\n'.join(lines)
    
    def save_to_file(self, filename: str) -> None:
        """
        Save references to a JSON file.
        
        Args:
            filename: Output filename
        """
        with open(filename, 'w', encoding='utf-8') as f:
            json.dump(self.references, f, indent=2, ensure_ascii=False)
    
    def load_from_file(self, filename: str) -> None:
        """
        Load references from a JSON file.
        
        Args:
            filename: Input filename
        """
        with open(filename, 'r', encoding='utf-8') as f:
            self.references = json.load(f)
