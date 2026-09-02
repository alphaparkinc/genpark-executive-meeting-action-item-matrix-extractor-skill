from client import ExecutiveMeetingActionItemMatrixExtractorClient

def main():
    client = ExecutiveMeetingActionItemMatrixExtractorClient()
    res = client.extract_action_items('John to deploy patch tonight.', 'Sprint Retrospective')
    print('Meeting Action Item Matrix Extractor: ' + res['meeting_extraction_id'] + ' (' + res['meeting_title'] + ')')
    print('Action Items: ' + str(len(res['extracted_action_items'])) + ' tasks assigned | Decisions: ' + str(res['decisions_recorded_count']))
    print('Matrix URL: ' + res['accountability_matrix_url'])

if __name__ == '__main__':
    main()
