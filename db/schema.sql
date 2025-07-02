-- users
CREATE TABLE users (
  id UUID PRIMARY KEY,
  username TEXT,
  created_at TIMESTAMP DEFAULT now()
);

-- sessions
CREATE TABLE sessions (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  started_at TIMESTAMP DEFAULT now()
);

-- chat_logs
CREATE TABLE chat_logs (
  id UUID PRIMARY KEY,
  session_id UUID REFERENCES sessions(id),
  message TEXT,
  sender TEXT,
  created_at TIMESTAMP DEFAULT now()
);

-- memory_embeddings
CREATE TABLE memory_embeddings (
  id UUID PRIMARY KEY,
  user_id UUID REFERENCES users(id),
  embedding double precision[],
  content TEXT,
  created_at TIMESTAMP DEFAULT now()
); 