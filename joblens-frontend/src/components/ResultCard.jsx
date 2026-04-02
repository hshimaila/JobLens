import SkillSection from "./SkillSection";
import MatchChart from "./MatchChart";

export default function ResultCard({ result }) {
  return (
    <div className="bg-white p-6 rounded-xl shadow-lg mt-6">

      <div className="grid md:grid-cols-2 gap-6 items-center">

        <MatchChart score={result.match_score} />

        <div>
          <h2 className="text-xl font-semibold">
            Your profile matches {result.match_score}% of this job
          </h2>
        </div>

      </div>
      {/* Skills */}
      <div className="grid md:grid-cols-2 gap-6">
        <SkillSection
          title="Matched Skills"
          skills={result.matched_skills}
          type="matched"
        />

        <SkillSection
          title="Missing Skills"
          skills={result.missing_skills}
          type="missing"
        />
      </div>
    </div>
  );
}