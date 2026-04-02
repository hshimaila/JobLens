export default function ResultCard({ result }) {
  const score = result.match_score;
  const circumference = 251.2;
  const offset = circumference - (score / 100) * circumference;
  const ringColor = score >= 70 ? "#1D9E75" : score >= 40 ? "#BA7517" : "#D85A30";
  const subtext = score >= 80 ? "Strong match! You are well-qualified for this role."
    : score >= 60 ? "Good match. A few skills to work on."
    : score >= 40 ? "Moderate match. Consider upskilling in the missing areas."
    : "Low match. Significant skill gaps to address.";

  return (
    <div className="space-y-4 mt-6">

      {/* Score */}
      <div className="bg-white border border-gray-100 rounded-2xl p-6 flex items-center gap-8">
        <div className="relative w-24 h-24 flex-shrink-0">
          <svg width="96" height="96" viewBox="0 0 100 100"
            style={{ transform: "rotate(-90deg)" }}>
            <circle cx="50" cy="50" r="40" fill="none"
              stroke="#F3F4F6" strokeWidth="10"/>
            <circle cx="50" cy="50" r="40" fill="none"
              stroke={ringColor} strokeWidth="10" strokeLinecap="round"
              strokeDasharray="251.2"
              strokeDashoffset={offset}
              style={{ transition: "stroke-dashoffset 1s ease" }}
            />
          </svg>
          <div className="absolute inset-0 flex flex-col items-center justify-center">
            <span className="text-2xl font-black text-gray-900 leading-none"
              style={{ fontFamily: "'Syne', sans-serif" }}>
              {score}%
            </span>
            <span className="text-[10px] text-gray-400 font-medium uppercase tracking-wide">
              match
            </span>
          </div>
        </div>
        <div>
          <h2 className="text-lg font-bold text-gray-900 mb-1"
            style={{ fontFamily: "'Syne', sans-serif" }}>
            Your profile matches {score}% of this job
          </h2>
          <p className="text-sm text-gray-500">{subtext}</p>
        </div>
      </div>

      {/* Skills */}
      <div className="grid md:grid-cols-2 gap-4">
        <div className="bg-white border border-gray-100 rounded-2xl p-5">
          <p className="text-xs font-medium text-emerald-700 uppercase tracking-widest mb-3">
            Matched Skills
          </p>
          <div className="flex flex-wrap gap-2">
            {result.matched_skills.map((s, i) => (
              <span key={i}
                className="text-xs px-3 py-1.5 rounded-full bg-emerald-50 text-emerald-700 font-medium">
                {s}
              </span>
            ))}
          </div>
        </div>
        <div className="bg-white border border-gray-100 rounded-2xl p-5">
          <p className="text-xs font-medium text-orange-700 uppercase tracking-widest mb-3">
            Missing Skills
          </p>
          <div className="flex flex-wrap gap-2">
            {result.missing_skills.map((s, i) => (
              <span key={i}
                className="text-xs px-3 py-1.5 rounded-full bg-orange-50 text-orange-700 font-medium">
                {s}
              </span>
            ))}
          </div>
        </div>
      </div>
    </div>
  );
}