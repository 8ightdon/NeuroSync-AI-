import React from 'react';

const SettingsPanel: React.FC = () => {
  return (
    <aside className="w-64 bg-white border-l p-4 hidden md:block">
      <h2 className="text-lg font-bold mb-4">Settings</h2>
      <div className="space-y-2">
        <div>
          <label className="block text-sm font-medium">Model</label>
          <select className="w-full border rounded px-2 py-1">
            <option>Mistral-7B</option>
            <option>LLaMA 3</option>
            <option>Phi-2</option>
          </select>
        </div>
        <div>
          <label className="block text-sm font-medium">Persona</label>
          <input className="w-full border rounded px-2 py-1" placeholder="e.g. Friendly" />
        </div>
      </div>
    </aside>
  );
};

export default SettingsPanel; 