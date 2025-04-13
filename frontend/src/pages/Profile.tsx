import { useState } from 'react'

const Profile = () => {
  const [user, setUser] = useState({
    username: 'johndoe',
    email: 'john@example.com',
    balance: 1000,
    totalBets: 15,
    wonBets: 8,
    lostBets: 5,
    pendingBets: 2,
  })

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-6">My Profile</h1>
      <div className="bg-white p-6 rounded-lg shadow-md">
        <div className="grid grid-cols-1 md:grid-cols-2 gap-6">
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              Account Information
            </h2>
            <div className="space-y-3">
              <div>
                <p className="text-gray-600">Username</p>
                <p className="font-medium">{user.username}</p>
              </div>
              <div>
                <p className="text-gray-600">Email</p>
                <p className="font-medium">{user.email}</p>
              </div>
              <div>
                <p className="text-gray-600">Balance</p>
                <p className="text-2xl font-bold text-primary-600">
                  ${user.balance}
                </p>
              </div>
            </div>
          </div>
          <div>
            <h2 className="text-xl font-semibold text-gray-900 mb-4">
              Betting Statistics
            </h2>
            <div className="grid grid-cols-2 gap-4">
              <div className="bg-gray-50 p-4 rounded-lg">
                <p className="text-gray-600">Total Bets</p>
                <p className="text-2xl font-bold">{user.totalBets}</p>
              </div>
              <div className="bg-green-50 p-4 rounded-lg">
                <p className="text-gray-600">Won Bets</p>
                <p className="text-2xl font-bold text-green-600">
                  {user.wonBets}
                </p>
              </div>
              <div className="bg-red-50 p-4 rounded-lg">
                <p className="text-gray-600">Lost Bets</p>
                <p className="text-2xl font-bold text-red-600">
                  {user.lostBets}
                </p>
              </div>
              <div className="bg-yellow-50 p-4 rounded-lg">
                <p className="text-gray-600">Pending Bets</p>
                <p className="text-2xl font-bold text-yellow-600">
                  {user.pendingBets}
                </p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </div>
  )
}

export default Profile 