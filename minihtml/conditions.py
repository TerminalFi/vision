from typing import Any, Callable, List


def when(condition: Any, *funcs: Callable[[], Any]) -> List[Any]:
    if condition:
        return [func() for func in funcs]
    else:
        return []


def when_or_else(
    condition: Any,
    funcs_when: List[Callable[[], Any]],
    funcs_else: List[Callable[[], Any]],
) -> List[Any]:
    if condition:
        return [func() for func in funcs_when]
    else:
        return [func() for func in funcs_else]
