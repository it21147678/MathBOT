import React from 'react';
import { useNavigate } from 'react-router-dom';

export default function WelcomeScreen() {
  const navigate = useNavigate();

  return (
    <div className="flex items-center justify-center h-screen bg-[#2a2b32]">
      <div className="text-center">
        <h1 className="text-white text-2xl mb-4">Welcome to Gen AI-Tutor</h1>
        <div className="flex justify-center space-x-4">
          <button
            className="px-5 py-2 bg-[#be7d26] text-white rounded hover:bg-[#eea647]"
            onClick={() => navigate('/login')}
          >
            Log in
          </button>
          <button
            className="px-4 py-2 bg-blue-900 text-white rounded hover:bg-blue-700"
            onClick={() => navigate('/register')}
          >
            Sign up
          </button>
        </div>
      </div>
    </div>
  );
}
