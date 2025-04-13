import { useState } from 'react'

interface Event {
  id: number
  title: string
  game: string
  teamA: string
  teamB: string
  oddsA: number
  oddsB: number
  startTime: string
  status: 'upcoming' | 'live' | 'completed'
}

const Events = () => {
  const [events, setEvents] = useState<Event[]>([
    {
      id: 1,
      title: 'League of Legends Championship',
      game: 'League of Legends',
      teamA: 'Team Faker',
      teamB: 'Team Caps',
      oddsA: 1.5,
      oddsB: 2.5,
      startTime: '2024-04-15 18:00',
      status: 'upcoming',
    },
    // Add more sample events as needed
  ])

  return (
    <div>
      <h1 className="text-3xl font-bold text-gray-900 mb-6">E-Sports Events</h1>
      <div className="grid gap-6">
        {events.map((event) => (
          <div
            key={event.id}
            className="bg-white p-6 rounded-lg shadow-md hover:shadow-lg transition-shadow"
          >
            <div className="flex justify-between items-start">
              <div>
                <h2 className="text-xl font-semibold text-gray-900">
                  {event.title}
                </h2>
                <p className="text-gray-600">{event.game}</p>
                <div className="mt-4 flex space-x-4">
                  <div className="text-center">
                    <p className="font-medium">{event.teamA}</p>
                    <p className="text-primary-600 font-bold">
                      {event.oddsA.toFixed(2)}
                    </p>
                  </div>
                  <div className="text-center">
                    <p className="text-gray-500">VS</p>
                  </div>
                  <div className="text-center">
                    <p className="font-medium">{event.teamB}</p>
                    <p className="text-primary-600 font-bold">
                      {event.oddsB.toFixed(2)}
                    </p>
                  </div>
                </div>
              </div>
              <div className="text-right">
                <span
                  className={`px-2 py-1 rounded-full text-xs font-medium ${
                    event.status === 'upcoming'
                      ? 'bg-yellow-100 text-yellow-800'
                      : event.status === 'live'
                      ? 'bg-green-100 text-green-800'
                      : 'bg-gray-100 text-gray-800'
                  }`}
                >
                  {event.status}
                </span>
                <p className="text-gray-500 mt-2">
                  {new Date(event.startTime).toLocaleString()}
                </p>
              </div>
            </div>
            <button className="mt-4 w-full bg-primary-600 text-white py-2 px-4 rounded-md hover:bg-primary-700 transition-colors">
              Place Bet
            </button>
          </div>
        ))}
      </div>
    </div>
  )
}

export default Events 