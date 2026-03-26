from time import perf_counter

from prometheus_client import CONTENT_TYPE_LATEST, Counter, Histogram, generate_latest
from starlette.middleware.base import BaseHTTPMiddleware
from starlette.requests import Request
from starlette.responses import Response

REQUEST_COUNT = Counter(
    "http_requests_total",
    "Total number of HTTP requests",
    ["method", "path", "status"],
)

REQUEST_LATENCY = Histogram(
    "http_request_duration_seconds",
    "HTTP request latency in seconds",
    ["method", "path"],
)


class PrometheusMiddleware(BaseHTTPMiddleware):
    async def dispatch(self, request: Request, call_next):
        # Skip self-scraping to reduce noisy metrics.
        if request.url.path == "/metrics":
            return await call_next(request)

        method = request.method
        path = request.url.path
        start = perf_counter()

        response = await call_next(request)

        duration = perf_counter() - start
        REQUEST_COUNT.labels(method=method, path=path, status=response.status_code).inc()
        REQUEST_LATENCY.labels(method=method, path=path).observe(duration)

        return response


def metrics_response() -> Response:
    return Response(content=generate_latest(), media_type=CONTENT_TYPE_LATEST)
