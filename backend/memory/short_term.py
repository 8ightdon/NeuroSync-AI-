# Short-term memory (session-based, in-memory)

class ShortTermMemory:
    def __init__(self):
        self.sessions = {}

    def get(self, session_id):
        return self.sessions.get(session_id, [])

    def add(self, session_id, message):
        if session_id not in self.sessions:
            self.sessions[session_id] = []
        self.sessions[session_id].append(message)
        # Limit to last N messages
        self.sessions[session_id] = self.sessions[session_id][-20:] 