// static/app.js
function nextStatus(current) {
  const order = ["planned","done","partial","missed","none"];
  const i = order.indexOf(current);
  return order[(i + 1) % order.length];
}

document.addEventListener("click", async (e) => {
  const cell = e.target.closest("[data-day-id]");
  if (!cell) return;

  const dayId = cell.dataset.dayId;
  const status = nextStatus(cell.dataset.status);

  const res = await fetch("/day/status", {
    method: "POST",
    headers: {"Content-Type":"application/json"},
    body: JSON.stringify({ day_id: Number(dayId), status })
  });
  const j = await res.json();
  if (j.ok) {
    cell.dataset.status = status;
    cell.className = "day " + status;
  } else {
    alert(j.error || "update failed");
  }
});
