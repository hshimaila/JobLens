export default function SkillSection({ title, skills, type }) {
  return (
    <div>
      <h3
        className={`font-bold mb-2 ${
          type === "matched" ? "text-green-600" : "text-red-600"
        }`}
      >
        {title}
      </h3>

      <div className="flex flex-wrap gap-2">
        {skills.map((skill, i) => (
          <span
            key={i}
            className={`px-3 py-1 rounded-full text-sm ${
              type === "matched"
                ? "bg-green-200 text-green-800"
                : "bg-red-200 text-red-800"
            }`}
          >
            {skill}
          </span>
        ))}
      </div>
    </div>
  );
}