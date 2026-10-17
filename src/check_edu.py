from predict import predict_with_confidence

tests = [
    "Sunrise Institute 5000",
    "Greenfield University 12000",
    "Lakeview College 8000",
    "Swiggy order 450",
]

for t in tests:
    category, conf = predict_with_confidence(t)
    print(t, "->", category, round(float(conf), 2))