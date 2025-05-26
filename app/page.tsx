export default function Home() {
  return (
    <main className="min-h-screen bg-gray-50 p-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-blue-700 mb-6">Café Manager</h1>
        
        <nav className="flex justify-center space-x-4 mb-10">
          <a href="/menu" className="btn">Menu</a>
          <a href="/inventory" className="btn">Inventory</a>
          <a href="/reports" className="btn">Sales Reports</a>
        </nav>

        <div className="card">
          <h2 className="title">Welcome to the Café Manager Dashboard!</h2>
          <p className="text-gray-600">
            Use the navigation above to manage your café's menu, inventory, and sales reports.
          </p>
        </div>
      </div>
    </main>
  );
}
