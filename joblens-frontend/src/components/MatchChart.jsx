import { RadialBarChart, RadialBar, PolarAngleAxis } from "recharts";

export default function MatchChart({ score }) {
  const data = [
    {
      name: "Match",
      value: score,
      fill:
        score < 40
          ? "#ef4444"
          : score < 70
          ? "#facc15"
          : "#22c55e",
    },
  ];

  return (
    <div className="flex justify-center items-center">
      <RadialBarChart
        width={250}
        height={250}
        cx="50%"
        cy="50%"
        innerRadius="70%"
        outerRadius="100%"
        barSize={15}
        data={data}
      >
        <PolarAngleAxis type="number" domain={[0, 100]} tick={false} />
        <RadialBar dataKey="value" cornerRadius={10} />
        <text
          x="50%"
          y="50%"
          textAnchor="middle"
          dominantBaseline="middle"
          className="text-2xl font-bold"
        >
          {score}%
        </text>
      </RadialBarChart>
    </div>
  );
}