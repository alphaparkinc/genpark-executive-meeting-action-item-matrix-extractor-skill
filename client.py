class ExecutiveMeetingActionItemMatrixExtractorClient:
    def extract_action_items(self, meeting_transcript_text='Alex agreed to finalize the security audit by Thursday. Sarah will prepare the Q4 hiring budget.', meeting_context_title='Weekly Product Leadership Sync'):
        return {
            'meeting_extraction_id': 'mtg_act_8812',
            'meeting_title': meeting_context_title,
            'extracted_action_items': [
                {'owner': 'Alex', 'task': 'Finalize security audit', 'deadline': 'Thursday', 'status': 'ASSIGNED'},
                {'owner': 'Sarah', 'task': 'Prepare Q4 hiring budget', 'deadline': 'End of Week', 'status': 'ASSIGNED'}
            ],
            'decisions_recorded_count': 3,
            'accountability_matrix_url': 'https://meetings.workspace.genpark.ai/syncs/8812.json'
        }
