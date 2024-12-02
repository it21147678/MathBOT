import { BrowserRouter as Router, Routes, Route } from 'react-router-dom'
import Login from './pages/Login'
import Register from './pages/Register'
import Welcome from './pages/Welcome'
import Sidebar from './components/layout/Sidebar'
import WelcomeScreen from './pages/WelcomeScreen'

export default function App() {
  return (
    <Router>
      <Routes>
      <Route path="/" element={<WelcomeScreen />} />
        <Route path="/home" element={<Welcome />} />
        <Route path="/login" element={<Login />} />
        <Route path="/register" element={<Register />} />
      </Routes>
    </Router>

  )
}