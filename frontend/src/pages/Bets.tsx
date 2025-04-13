import { useState } from 'react'

interface Bet {
  id: number
  eventTitle: string
  team: string
  amount: number
  potentialWin: number
  status: 'pending' | 'won' | 'lost'
  placedAt: string
}

const Bets = () => {
  const [bets, setBets] = useState<Bet[]>([
    {
      id: 1,
      eventTitle: 'League of Legends Championship',
      team: 'Team Faker',
      amount: 100,
      potentialWin: 150,
      status: 'pending',
      placedAt: '2024-04-10 15:30',
    },
    // Add more sample bets as needed
  ])

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-6">My Bets</h1>
      <div className="grid gap-6">
        {bets.map((bet) => (
          <div
            key={bet.id}
            className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
          >
            <div className="flex justify-between items-start">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">
                  {bet.eventTitle}
                </h2>
                <p className="text-gray-600">Team: {bet.team}</p>
                <div className="mt-4">
                  <p className="text-gray-600">
                    Amount: <span className="font-medium">${bet.amount}</span>
                  </p>
                  <p className="text-gray-600">
                    Potential Win:{' '}
                    <span className="font-medium">${bet.potentialWin}</span>
                  </p>
                </div>
              </div>
              <div className="text-right">
                <span
                  className={`px-2 py-1 rounded-full text-xs font-medium ${
                    bet.status === 'pending'
                      ? 'bg-yellow-100 text-yellow-800'
                      : bet.status === 'won'
                      ? 'bg-green-100 text-green-800'
                      : 'bg-red-100 text-red-800'
                  }`}
                >
                  {bet.status}
                </span>
                <p className="text-gray-500 mt-2">
                  {new Date(bet.placedAt).toLocaleString()}
                </p>
              </div>
            </div>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Bets 