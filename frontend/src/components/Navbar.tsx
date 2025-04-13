import { Link } from 'react-router-dom'

const Navbar = () => {
  return (
    <nav className="bg-white shadow-lg">
      <div className="container mx-auto px-4">
        <div className="flex justify-between items-center h-16">
          <Link to="/" className="text-2xl font-bold text-primary-600">
            EasyBet
          </Link>
          <div className="flex space-x-4">
            <Link
              to="/events"
              className="text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            >
              Events
            </Link>
            <Link
              to="/bets"
              className="text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            >
              My Bets
            </Link>
            <Link
              to="/profile"
              className="text-gray-600 hover:text-primary-600 px-3 py-2 rounded-md text-sm font-medium"
            >
              Profile
            </Link>
          </div>
        </div>
      </div>
    </nav>
  )
}

export default Navbar 