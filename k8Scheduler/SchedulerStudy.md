# Scheduler Study

## predicatesOrdering

[CheckNodeConditionPredicate](https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/algorithm/predicates/predicates.go#L1675)
```
This Algorithm checks if a pod can be scheduled on a node reporting
network unavailable and not ready condition. Only node conditions are accounted in this predicate.

// We consider the node for scheduling only when its:
// - NodeReady condition status is ConditionTrue,
// - NodeNetworkUnavailable condition status is ConditionFalse.
```

[CheckNodeMemoryPressurePredicate](https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/algorithm/predicates/predicates.go#L1633)
```
This Algorithm reporting memory pressure condition.
// check if node is under memory pressure
```

[MatchInterPodAffinity](http://wsfdl.com/kubernetes/2018/06/30/k8s-scheduler-1-affinity.html)<br/>
[Official Link](https://kubernetes.io/docs/concepts/configuration/assign-pod-node/#affinity-and-anti-affinity)
```
我们常常会收到亲和性／反亲和性相关的需求。亲和性多用于实现业务的就近部署，减少网络，降低延时；反亲和性多用于故障容灾，从多个维度分散实例，尽可能降低故障影响的同类业务实例数量，特别是数据存储类的业务，它们对反亲和性的需求往往很强烈。从硬件资源拓扑角度来看，每个机架(rack)约有十多台的物理机和一(两)台接入交换机，这些接入交换机连接到汇聚交换机，汇聚交换机再连接到核心交换机。一般来说，汇聚交换机和核心交换机都会从硬件层面实现高可靠。我们遇上了多种故障，最常见的是主机硬件故障，此外还有四子星机器电源故障，机柜电源故障，接入交换机故障等等。并非所有的机柜都做到双电源，并非所有的接入交换机都有冗余。所以机柜电源故障和接入交换机故障往往会影响整个机柜的实例。所以一般的业务方要求实例部署在不同的机器，特殊的业务方，如 DB 等等，需要将相同 DB 的实例分布在不同的机柜。此外因链路割接，故障演练等因素，某些业务还需要在有异地机房冗余。
```

## prioritiesOrdering

[OfficialLink](https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/algorithm/priorities/priorities.go)<br/>

[LeastRequestedPriority](https://github.com/kubernetes/kubernetes/tree/master/pkg/scheduler/algorithm/priorities)
```
LeastRequestedPriorityMap is a priority function that favors nodes with fewer requested resources.
It calculates the percentage of memory and CPU requested by pods scheduled on the node, and
prioritizes based on the minimum of the average of the fraction of requested to capacity.

Details:
(cpu((capacity-sum(requested))*10/capacity) + memory((capacity-sum(requested))*10/capacity))/2

--eviction-hard=[memory.available<500Mi]

Link: https://zhuanlan.zhihu.com/p/38359775
kubelet 目前把 cadvisor 的大量代码直接作为 vendor 引入。其实就相当于在 kubelet 内部启动了一个小的 cadvisor。在 kubelet 启动后，这个内部的 cadvisor 子模块也会相应启动，并且获取这台机器上面的各种信息。其中就包括了有关这台机器的资源信息，而这个信息也自然作为这台机器的真实资源信息，通过 kubelet 再上报给 apiserver。
```

[BalancedResourceAllocation](https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/algorithm/priorities/balanced_resource_allocation.go)
```
// BalancedResourceAllocationMap favors nodes with balanced resource usage rate.
// BalancedResourceAllocationMap should **NOT** be used alone, and **MUST** be used together
// with LeastRequestedPriority. It calculates the difference between the cpu and memory fraction
// of capacity, and prioritizes the host based on how close the two metrics are to each other.
// Detail: score = 10 - variance(cpuFraction,memoryFraction,volumeFraction)*10. The algorithm is partly inspired by:

"Wei Huang et al. An Energy Efficient Virtual Machine Placement Algorithm with Balanced Resource Utilization"
```

[InterPodAffinityPriority](https://github.com/kubernetes/kubernetes/blob/master/pkg/scheduler/algorithm/priorities/interpod_affinity.go)
```
// CalculateInterPodAffinityPriority compute a sum by iterating through the elements of weightedPodAffinityTerm and adding
// "weight" to the sum if the corresponding PodAffinityTerm is satisfied for
// that node; the node(s) with the highest sum are the most preferred.
// Symmetry need to be considered for preferredDuringSchedulingIgnoredDuringExecution from podAffinity & podAntiAffinity,
// symmetry need to be considered for hard requirements from podAffinity
```

