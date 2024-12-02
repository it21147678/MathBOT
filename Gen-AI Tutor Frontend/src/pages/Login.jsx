import { useState } from 'react';
import { useNavigate, Link } from 'react-router-dom';
import { Mail, Lock } from 'lucide-react';

export default function Login() {
  const navigate = useNavigate();
  const [email, setEmail] = useState('');
  const [password, setPassword] = useState('');

  const handleSubmit = (e) => {
    e.preventDefault();
    // Add authentication logic here
    navigate('/home'); // Navigate to the /home page
  };

  return (
    <div className="min-h-screen flex items-center justify-center bg-white p-4">
      <div className="max-w-md space-y-8 items-center">
        {/* Header */}
        <div className="text-center">
          <h2 className="mt-6 text-[31px] font-[700] text-[#13254d]">
            Hey Welcome Back
          </h2>
        </div>
        
        <form className="mt-8 space-y-6 w-[320px] items-center ml-2" onSubmit={handleSubmit}>
          
          <div className="relative">
            <div className="relative">
              <div className="absolute -top-2 flex items-center w-full">
                <span className="text-[14px] text-[#1b428a] bg-white pr-2 pl-2">
                  Email address
                </span>
                <div className="flex-grow h-[1px]"></div>
              </div>
             
              <input
                type="email"
                value={email}
                onChange={(e) => setEmail(e.target.value)}
                className="w-full mt-2 px-3 py-2 border-2 border-[#1b428a] rounded-md focus:outline-none focus:border-blue-700"
                placeholder=""
              />
            </div>
          </div>
            
          <div className="relative h-[64px]">
            <div className="relative">
              {/* Label with line */}
              <div className="absolute -top-2 flex items-center w-full">
                <span className="text-[14px] text-[#1b428a] bg-white pl-2 pr-2">
                  Password
                </span>
                <div className="flex-grow- h-[1px]"></div>
              </div>

              {/* Input */}
              <input
                type="password"
                value={password}
                onChange={(e) => setPassword(e.target.value)}
                className="w-full mt-2 px-3 py-2 border-2 border-[#1b428a] rounded-md focus:outline-none focus:border-blue-700"
                placeholder=""
              />
            </div>
          </div>

          {/* Continue Button */}
          <button
            type="submit"
            className="group relative w-full h-10 flex justify-center py-2 px-4 border border-transparent text-[15px] font-medium rounded-md text-white bg-[#1b428a] hover:bg-[#25488a] focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-[#00B894]"
          >
            Continue
          </button>

          <p className="text-center text-sm text-gray-400">
            Don't have an account?{' '}
            <Link to="/register" className="font-medium text-blue-900 hover:text-blue-700">
              Sign up
            </Link>
          </p>

          <div className="relative my-4">
            <div className="absolute inset-0 flex items-center">
              <div className="w-full border-t border-gray-400"></div>
            </div>
            <div className="relative flex justify-center text-sm px-4">
              <span className="bg-white px-2  text-gray-400">OR</span>
            </div>
          </div>

          <div className="space-y-3">
            <button
              type="button"
              className="w-full flex items-center justify-left px-4 py-2 border border-gray-700 rounded-md shadow-sm text-sm font-small text-gray-700  hover:bg-gray-700 hover:text-white"
            >
              <img 
                src="/Google Logo.svg" 
                alt="Google" 
                className="h-5 w-5 mr-2"
              />
              Continue with Google
            </button>
            <button
              type="button"
              className="w-full flex items-center justify-left px-4 py-2 border border-gray-700 rounded-md shadow-sm text-sm font-small text-gray-700  hover:bg-gray-700 hover:text-white"
            >
              <img 
                src="/Microsoft Logo.svg" 
                alt="Microsoft" 
                className="h-5 w-5 mr-2"
              />
              Continue with Microsoft Account
            </button>
          </div>
        </form>
      </div>
    </div>
  );
}
