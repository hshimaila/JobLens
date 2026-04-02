export default function Navbar() {
  return (
    <div className="bg-white shadow-md p-4 flex justify-between items-center">
      <h1 className="text-xl font-bold text-blue-600">JobLens</h1>
      <button className="bg-blue-600 text-white px-4 py-1 rounded-lg">
        Analyze
      </button>
    </div>
  );
}