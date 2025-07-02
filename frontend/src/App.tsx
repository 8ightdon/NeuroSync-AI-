import React from 'react';
import ChatInput from './components/ChatInput';
import ChatBubble from './components/ChatBubble';
import SidebarMemory from './components/SidebarMemory';
import SettingsPanel from './components/SettingsPanel';

const App = () => {
  return (
    <div className="flex h-screen bg-gray-100">
      <SidebarMemory />
      <div className="flex flex-col flex-1">
        <div className="flex-1 overflow-y-auto p-4">
          {/* Chat bubbles would be mapped here */}
          <ChatBubble message="Hello! How can I help you today?" sender="ai" />
        </div>
        <ChatInput />
      </div>
      <SettingsPanel />
    </div>
  );
};

export default App; 