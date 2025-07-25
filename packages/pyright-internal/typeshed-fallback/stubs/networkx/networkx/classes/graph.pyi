from _typeshed import Incomplete
from collections.abc import Callable, Collection, Hashable, Iterable, Iterator, Mapping, MutableMapping
from functools import cached_property
from typing import Any, ClassVar, TypeVar, overload
from typing_extensions import Self, TypeAlias

import numpy
from networkx.classes.coreviews import AdjacencyView, AtlasView
from networkx.classes.digraph import DiGraph
from networkx.classes.reportviews import DegreeView, DiDegreeView, NodeView, OutEdgeView

_Node = TypeVar("_Node", bound=Hashable)
_NodeWithData: TypeAlias = tuple[_Node, dict[str, Any]]
_NodePlus: TypeAlias = _Node | _NodeWithData[_Node]
_Edge: TypeAlias = tuple[_Node, _Node]
_EdgeWithData: TypeAlias = tuple[_Node, _Node, dict[str, Any]]
_EdgePlus: TypeAlias = _Edge[_Node] | _EdgeWithData[_Node]
_MapFactory: TypeAlias = Callable[[], MutableMapping[str, Any]]
_NBunch: TypeAlias = _Node | Iterable[_Node] | None
_Data: TypeAlias = (
    Graph[_Node]
    | dict[_Node, dict[_Node, dict[str, Any]]]
    | dict[_Node, Iterable[_Node]]
    | Iterable[_EdgePlus[_Node]]
    | numpy.ndarray[Any, Any]
    # | scipy.sparse.base.spmatrix
)

__all__ = ["Graph"]

class Graph(Collection[_Node]):
    __networkx_backend__: ClassVar[str]
    node_dict_factory: ClassVar[_MapFactory]
    node_attr_dict_factory: ClassVar[_MapFactory]
    adjlist_outer_dict_factory: ClassVar[_MapFactory]
    adjlist_inner_dict_factory: ClassVar[_MapFactory]
    edge_attr_dict_factory: ClassVar[_MapFactory]
    graph_attr_dict_factory: ClassVar[_MapFactory]

    graph: dict[str, Any]

    def to_directed_class(self) -> type[DiGraph[_Node]]: ...
    def to_undirected_class(self) -> type[Graph[_Node]]: ...
    def __init__(self, incoming_graph_data: _Data[_Node] | None = None, **attr) -> None: ...
    @cached_property
    def adj(self) -> AdjacencyView[_Node, _Node, dict[str, Incomplete]]: ...
    @property
    def name(self) -> str: ...
    @name.setter
    def name(self, s: str) -> None: ...
    def __getitem__(self, n: _Node) -> AtlasView[_Node, str, Any]: ...
    def __iter__(self) -> Iterator[_Node]: ...
    def __contains__(self, n: object) -> bool: ...
    def __len__(self) -> int: ...
    def add_node(self, node_for_adding: _Node, **attr: Any) -> None: ...  # attr: Set or change node attributes using key=value
    def add_nodes_from(self, nodes_for_adding: Iterable[_NodePlus[_Node]], **attr) -> None: ...
    def remove_node(self, n: _Node) -> None: ...
    def remove_nodes_from(self, nodes: Iterable[_Node]) -> None: ...
    @cached_property
    def nodes(self) -> NodeView[_Node]: ...
    def number_of_nodes(self) -> int: ...
    def order(self) -> int: ...
    def has_node(self, n: _Node) -> bool: ...
    # attr: Edge data (or labels or objects) can be assigned using keyword arguments
    def add_edge(self, u_of_edge: _Node, v_of_edge: _Node, **attr: Any) -> None: ...
    def add_edges_from(self, ebunch_to_add: Iterable[_EdgePlus[_Node]], **attr) -> None: ...
    def add_weighted_edges_from(
        self, ebunch_to_add: Iterable[tuple[_Node, _Node, Incomplete]], weight: str = "weight", **attr
    ) -> None: ...
    def remove_edge(self, u: _Node, v: _Node) -> None: ...
    def remove_edges_from(self, ebunch: Iterable[_EdgePlus[_Node]]) -> None: ...
    @overload
    def update(self, edges: Graph[_Node], nodes: None = None) -> None: ...
    @overload
    def update(
        self, edges: Graph[_Node] | Iterable[_EdgePlus[_Node]] | None = None, nodes: Iterable[_Node] | None = None
    ) -> None: ...
    def has_edge(self, u: _Node, v: _Node) -> bool: ...
    def neighbors(self, n: _Node) -> Iterator[_Node]: ...
    @cached_property
    def edges(self) -> OutEdgeView[_Node]: ...
    def get_edge_data(self, u: _Node, v: _Node, default=None) -> Mapping[str, Incomplete]: ...
    def adjacency(self) -> Iterator[tuple[_Node, Mapping[_Node, Mapping[str, Incomplete]]]]: ...
    @cached_property
    def degree(self) -> DegreeView[_Node] | DiDegreeView[_Node]: ...  # Include subtypes' possible return types
    def clear(self) -> None: ...
    def clear_edges(self) -> None: ...
    def is_multigraph(self) -> bool: ...
    def is_directed(self) -> bool: ...
    def copy(self, as_view: bool = False) -> Self: ...
    def to_directed(self, as_view: bool = False) -> DiGraph[_Node]: ...
    def to_undirected(self, as_view: bool = False) -> Graph[_Node]: ...
    def subgraph(self, nodes: Iterable[_Node]) -> Graph[_Node]: ...
    def edge_subgraph(self, edges: Iterable[_Edge[_Node]]) -> Graph[_Node]: ...
    @overload
    def size(self, weight: None = None) -> int: ...
    @overload
    def size(self, weight: str) -> float: ...
    def number_of_edges(self, u: _Node | None = None, v: _Node | None = None) -> int: ...
    def nbunch_iter(self, nbunch: _NBunch[_Node] = None) -> Iterator[_Node]: ...
