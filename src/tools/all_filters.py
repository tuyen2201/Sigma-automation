import os
import yaml

# Get the project root directory
PROJECT_ROOT = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

rules_dir = os.path.join(PROJECT_ROOT, "data", "rules", "windows", "process_creation")
selected_rules_file = os.path.join(PROJECT_ROOT, "data", "evasion_possible_rules.txt")
output_file = os.path.join(PROJECT_ROOT, "output", "results", "extracted_filters.txt")

# Ensure output directory exists
os.makedirs(os.path.dirname(output_file), exist_ok=True)

with open(selected_rules_file, "r", encoding="utf-8") as f:
    rule_names = [line.strip() for line in f if line.strip()]
    rule_files = [name if name.endswith(".yml") else f"{name}.yml" for name in rule_names]

filters = []

for rule_file in rule_files:
    rule_path = os.path.join(rules_dir, rule_file)
    if not os.path.isfile(rule_path):
        print(f"[!] File not found: {rule_path}")
        continue

    try:
        with open(rule_path, "r", encoding="utf-8") as f:
            all_docs = yaml.safe_load_all(f)
            for idx, doc in enumerate(all_docs):
                if not isinstance(doc, dict):
                    continue
                rule_filter = doc.get("filter")
                if rule_filter is None:
                    rule_filter = doc.get("detection", {}).get("selection")
                if rule_filter is None:
                    rule_filter = doc.get("detection", {}).get("filter")
                if rule_filter is not None:
                    filters.append(f"# {rule_file} (doc {idx + 1})\n{rule_filter}\n")
                else:
                    print(f"[!] Không tìm thấy filter trong: {rule_file} (doc {idx + 1})")
    except Exception as e:
        print(f"[!] Lỗi đọc {rule_file}: {e}")

with open(output_file, "w", encoding="utf-8") as f:
    f.write("\n---\n".join(filters))

print(f"\n✅ Đã xuất {len(filters)} filter vào file: {output_file}")
