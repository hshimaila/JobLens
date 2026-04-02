export default function Suggestions({ suggestions }) {
  if (!suggestions || Object.keys(suggestions).length === 0) return null;

  return (
    <div className="bg-white border border-gray-100 rounded-2xl p-6 mt-4">
      <h2 className="text-lg font-bold text-gray-900 mb-5"
        style={{ fontFamily: "'Syne', sans-serif" }}>
        Learning Resources
      </h2>

      <div className="divide-y divide-gray-100">
        {Object.entries(suggestions).map(([skill, data], i) => (
          <div key={i} className="py-4 first:pt-0 last:pb-0">
            <p className="text-sm font-semibold text-blue-600 mb-2">{skill}</p>
            <div className="flex flex-wrap gap-2">
              {data.videos.map((v, idx) => (
                <a key={idx} href={v.link} target="_blank" rel="noopener noreferrer"
                  className="text-xs px-3 py-1.5 rounded-lg bg-red-50 text-red-700 font-medium hover:bg-red-100 transition-colors">
                  ▶ {v.title}
                </a>
              ))}
              {data.courses.map((c, idx) => (
                <a key={idx} href={c.link} target="_blank" rel="noopener noreferrer"
                  className="text-xs px-3 py-1.5 rounded-lg bg-blue-50 text-blue-700 font-medium hover:bg-blue-100 transition-colors">
                  ↗ {c.title}
                </a>
              ))}
            </div>
          </div>
        ))}
      </div>
    </div>
  );
}