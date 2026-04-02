export default function Suggestions({ suggestions }) {
  if (!suggestions || Object.keys(suggestions).length === 0) return null;

  return (
    <div className="bg-white/80 backdrop-blur-md p-6 rounded-2xl shadow-xl mt-6">
      <h2 className="text-xl font-bold mb-4">📚 Learning Suggestions</h2>

      {Object.entries(suggestions).map(([skill, data], i) => (
        <div key={i} className="mb-6">

          {/* Skill Title */}
          <h3 className="font-semibold text-blue-600 text-lg mb-2">
            {skill}
          </h3>

          {/* Videos */}
          <div className="mb-2">
            <p className="font-medium">🎥 Videos:</p>
            <ul className="ml-4 list-disc">
              {data.videos.map((v, idx) => (
                <li key={idx}>
                  <a
                    href={v.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-blue-500 hover:underline"
                  >
                    {v.title}
                  </a>
                </li>
              ))}
            </ul>
          </div>

          {/* Courses */}
          <div>
            <p className="font-medium">📘 Courses:</p>
            <ul className="ml-4 list-disc">
              {data.courses.map((c, idx) => (
                <li key={idx}>
                  <a
                    href={c.link}
                    target="_blank"
                    rel="noopener noreferrer"
                    className="text-green-600 hover:underline"
                  >
                    {c.title}
                  </a>
                </li>
              ))}
            </ul>
          </div>

        </div>
      ))}
    </div>
  );
}