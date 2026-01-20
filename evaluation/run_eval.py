from datasets import Dataset
from ragas import evaluate
from ragas.metrics import answer_relevancy, context_precision, faithfulness

# 1. Giả lập hoặc load tập dữ liệu kiểm thử (Ground Truth)
test_data = {
    "question": ["Làm thế nào để khởi tạo LangGraph?", "Hybrid Search là gì?"],
    "contexts": [
        ["Dùng StateGraph từ langgraph.graph..."],
        ["Kết hợp Vector và BM25..."],
    ],
    "answer": ["Bạn dùng StateGraph.", "Là sự kết hợp tìm kiếm dày đặc và thưa thớt."],
    "ground_truth": [
        "Để khởi tạo LangGraph, cần định nghĩa StateGraph và Nodes.",
        "Hybrid Search là kỹ thuật kết hợp giữa Vector Search và BM25.",
    ],
}


def run_assessment():
    dataset = Dataset.from_dict(test_data)

    # 2. Chạy đánh giá
    result = evaluate(
        dataset,
        metrics=[faithfulness, answer_relevancy, context_precision],
    )

    # 3. Xuất kết quả ra định dạng Markdown cho GitHub Action
    df = result.to_pandas()
    with open("report.md", "w") as f:
        f.write("### 📊 RAG Evaluation Report\n")
        f.write(df.to_markdown())


if __name__ == "__main__":
    run_assessment()
