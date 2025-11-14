"""
Paper Summarizer Module
Provides functionality to summarize research papers.
"""

from typing import Dict, List


class PaperSummarizer:
    """Summarize research papers into concise formats."""
    
    def __init__(self):
        """Initialize the paper summarizer."""
        pass
    
    def summarize_abstract(self, abstract: str, max_sentences: int = 3) -> str:
        """
        Summarize an abstract to key sentences.
        
        Args:
            abstract: The abstract text
            max_sentences: Maximum number of sentences to include
            
        Returns:
            Summarized abstract
        """
        if not abstract:
            return ""
        
        # Split into sentences
        sentences = [s.strip() for s in abstract.replace('\n', ' ').split('.') if s.strip()]
        
        # Return first max_sentences
        summary_sentences = sentences[:max_sentences]
        return '. '.join(summary_sentences) + '.'
    
    def extract_key_findings(self, results: str, max_points: int = 5) -> List[str]:
        """
        Extract key findings from results section.
        
        Args:
            results: The results section text
            max_points: Maximum number of key points to extract
            
        Returns:
            List of key findings
        """
        if not results:
            return []
        
        findings = []
        
        # Look for numbered or bulleted points
        lines = results.split('\n')
        for line in lines:
            line = line.strip()
            # Check for bullet points or numbered lists
            if line and (line[0] in '•-*' or (len(line) > 2 and line[0].isdigit() and line[1] in '.):')):
                findings.append(line.lstrip('•-*0123456789.): ').strip())
                if len(findings) >= max_points:
                    break
        
        # If no structured points found, extract sentences containing key result indicators
        if not findings:
            result_indicators = ['found', 'showed', 'demonstrated', 'revealed', 'indicated', 
                               'significant', 'increased', 'decreased', 'observed']
            sentences = [s.strip() for s in results.split('.') if s.strip()]
            
            for sentence in sentences:
                if any(indicator in sentence.lower() for indicator in result_indicators):
                    findings.append(sentence)
                    if len(findings) >= max_points:
                        break
        
        return findings[:max_points]
    
    def summarize_methods(self, methods: str) -> str:
        """
        Summarize the methodology section.
        
        Args:
            methods: The methods section text
            
        Returns:
            Summarized methods
        """
        if not methods:
            return ""
        
        # Extract first paragraph or first few sentences
        paragraphs = [p.strip() for p in methods.split('\n\n') if p.strip()]
        if paragraphs:
            first_para = paragraphs[0]
            sentences = [s.strip() for s in first_para.split('.') if s.strip()]
            return '. '.join(sentences[:3]) + '.'
        
        return ""
    
    def generate_paper_summary(self, paper_data: Dict) -> Dict[str, any]:
        """
        Generate a comprehensive summary of a paper.
        
        Args:
            paper_data: Dictionary containing paper information (from PaperProcessor)
            
        Returns:
            Dictionary containing summarized information
        """
        summary = {
            'title': paper_data.get('metadata', {}).get('title', 'Unknown'),
            'year': paper_data.get('metadata', {}).get('year', ''),
            'keywords': paper_data.get('metadata', {}).get('keywords', []),
            'abstract_summary': self.summarize_abstract(paper_data.get('abstract', '')),
            'methods_summary': self.summarize_methods(paper_data.get('methods', '')),
            'key_findings': self.extract_key_findings(paper_data.get('results', '')),
            'conclusion': paper_data.get('conclusion', '')[:500] if paper_data.get('conclusion') else ''
        }
        
        return summary
    
    def format_summary_text(self, summary: Dict) -> str:
        """
        Format a summary dictionary as readable text.
        
        Args:
            summary: Summary dictionary from generate_paper_summary
            
        Returns:
            Formatted text summary
        """
        text_parts = []
        
        text_parts.append(f"TITLE: {summary['title']}")
        if summary['year']:
            text_parts.append(f"YEAR: {summary['year']}")
        
        if summary['keywords']:
            text_parts.append(f"KEYWORDS: {', '.join(summary['keywords'])}")
        
        text_parts.append("\nABSTRACT SUMMARY:")
        text_parts.append(summary['abstract_summary'])
        
        if summary['methods_summary']:
            text_parts.append("\nMETHODS:")
            text_parts.append(summary['methods_summary'])
        
        if summary['key_findings']:
            text_parts.append("\nKEY FINDINGS:")
            for i, finding in enumerate(summary['key_findings'], 1):
                text_parts.append(f"{i}. {finding}")
        
        if summary['conclusion']:
            text_parts.append("\nCONCLUSION:")
            text_parts.append(summary['conclusion'])
        
        return '\n'.join(text_parts)
