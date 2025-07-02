import React from 'react';

const SidebarMemory: React.FC = () => {
  return (
    <aside className="w-64 bg-white border-r p-4 hidden md:block">
      <h2 className="text-lg font-bold mb-4">Memory</h2>
      <ul>
        <li className="mb-2 text-gray-700">No memory yet.</li>
      </ul>
    </aside>
  );
};

export default SidebarMemory; 