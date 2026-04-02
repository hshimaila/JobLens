export default function Navbar() {
  return (
    <nav style={{ fontFamily: "'DM Sans', sans-serif" }}
      className="bg-white border-b border-gray-100 px-8 h-14 flex items-center justify-between">
      <span className="text-[22px] font-black tracking-tight"
        style={{ fontFamily: "'Syne', sans-serif" }}>
        <span className="text-blue-600">Job</span>
        <span className="text-gray-900">Lens</span>
      </span>
      <span className="text-xs bg-blue-50 text-blue-600 px-3 py-1 rounded-full font-medium">
        AI-Powered
      </span>
    </nav>
  );
}