import Link from 'next/link';
export default function Home() {
  return (
    <main className="min-h-screen bg-gray-100 p-8">
      <div className="max-w-3xl mx-auto">
        <h1 className="text-4xl font-bold text-center text-red-950 mb-6">Café Manager</h1>
        
        <nav className="flex justify-center space-x-4 mb-10">
          <Link href="/menu" className="btn">Menu</Link>
          <Link href="/inventory" className="btn">Inventory</Link>
          <Link href="/reports" className="btn">Sales Reports</Link>
        </nav>

        <div className="card">
          <h2 className="title">Welcome!</h2>
          <p className="text-gray-600">
            Use the navigation above to manage your café's menu, inventory, and sales reports.
          </p>
        </div>
      </div>
    </main>
  );

}
