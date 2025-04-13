import { Link } from 'react-router-dom'

const Home = () => {
  return (
    <div className="text-center">
      <h1 className="text-4xl font-bold text-gray-900 mb-6">
        Welcome to EasyBet
      </h1>
      <p className="text-xl text-gray-600 mb-8">
        Your premier destination for e-sports betting
      </p>
      <div className="grid grid-cols-1 md:grid-cols-2 gap-6 max-w-4xl mx-auto">
        <Link
          to="/events"
          className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <h2 className="text-2xl font-semibold text-primary-600 mb-3">
            Upcoming Events
          </h2>
          <p className="text-gray-600">
            Browse and bet on upcoming e-sports events
          </p>
        </Link>
        <Link
          to="/bets"
          className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
        >
          <h2 className="text-2xl font-semibold text-primary-600 mb-3">
            My Bets
          </h2>
          <p className="text-gray-600">
            Track your active and completed bets
          </p>
        </Link>
      </div>
    </div>
  )
}

export default Home 