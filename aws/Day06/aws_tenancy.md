# Understanding AWS Tenancy Options: Shared Tenancy, Dedicated Hosts, and Dedicated Instances

When deploying applications on AWS, choosing the appropriate tenancy model is crucial for balancing cost, performance, and control. AWS offers three primary tenancy options: Shared Tenancy, Dedicated Hosts, and Dedicated Instances. Each option has distinct characteristics, benefits, and considerations. This article provides a detailed overview of these tenancy models, helping you make an informed decision based on your specific requirements.

## Shared Tenancy

Shared Tenancy is the default behavior for AWS instances, where multiple instances from various customers share the same physical hardware. This model allows AWS to optimize resource utilization and reduce costs by pooling resources across multiple customers.

### Characteristics:

- **Multiple instances on a physical machine**: Instances from different customers share the same physical hardware.
- **Default instance behavior**: Automatically used unless otherwise specified.
- **Time-sharing**: Resources are shared in a time-sliced manner, allowing multiple applications to run on the same hardware.

### Benefits:

- **Reduced costs**: Economies of scale allow for lower pricing compared to dedicated options.
- **Simpler deployment**: No need for specific configuration or management of physical hardware.

### Considerations:

#### Pros:
- **Cost-efficient**: Shared infrastructure reduces the overall cost of deployment.
- **Ease of use**: Deployment is straightforward without additional configuration.

#### Cons:
- **Lower performance**: Shared resources can lead to variable performance due to “noisy neighbors”.
- **Less control**: Limited ability to manage or influence the underlying physical hardware.

#### Hindrances:
- **Performance variability**: Resource contention can affect application performance.
- **Limited control**: Less influence over hardware management and allocation.

## Dedicated Hosts

Dedicated Hosts provide physical servers dedicated to a single customer. This option gives greater control over the underlying hardware, which can be beneficial for compliance, licensing, and performance management.

### Characteristics:

- **Physical machines running virtual instances**: Each host is a physical machine running instances for a single customer.
- **Used by one customer**: Entire physical host is allocated to a single customer, ensuring no other customer’s instances run on the same hardware.
- **Explicit configuration required**: Must be configured during instance setup.
- **Not available in the free tier**: Only available under paid plans.

### Benefits:

- **Better licensing management and reporting**: Facilitates more accurate tracking of software licenses.
- **Compliance management**: Helps meet regulatory and compliance requirements by controlling instance placement.
- **Host placement control**: Allows control over where instances are placed during restarts, enhancing stability and performance.

### Considerations:

#### Pros:
- **Accurate licensing management**: Helps maintain compliance with software licensing agreements.
- **Detailed reporting**: Provides more granular insights into host usage.
- **Compliance and control**: Essential for organizations with strict compliance requirements.
- **Control over host placement**: Greater control during instance restarts and migrations.

#### Cons:
- **Higher costs**: More expensive than shared tenancy due to dedicated resources.

## Dedicated Instances

Dedicated Instances offer a middle ground, providing instances that run on single-tenant hardware but without some of the additional control features of Dedicated Hosts.

### Characteristics:

- **Physical machine usage**: Instances run on a physical machine dedicated to one customer at a time.
- **Single customer usage**: Ensures no other customer’s instances share the same physical machine.
- **May move on restart**: Instances may be moved to a different physical machine on restart, unlike Dedicated Hosts.
- **Explicit configuration required**: Must be explicitly chosen during setup.
- **Not available in the free tier**: Requires a paid plan.

### Benefits:

- **Hardware dedication**: Ensures performance benefits similar to Dedicated Hosts by running on dedicated hardware.
- **Improved performance**: Provides performance advantages due to dedicated resources.

### Considerations:

#### Pros:
- **Dedicated hardware**: Ensures instances do not share physical resources with other customers.
- **Performance advantage**: Benefits from dedicated resources.

#### Cons:
- **Less accurate licensing management**: Does not provide the same level of licensing control as Dedicated Hosts.
- **No host placement control**: Lacks control over specific host placements during restarts.

## Conclusion

Choosing the right tenancy model in AWS depends on your organization’s specific cost, performance, control, and compliance needs.

- **Shared Tenancy** is ideal for cost-sensitive applications with flexible performance requirements, offering simplicity and reduced costs.
- **Dedicated Hosts** are best for applications requiring stringent compliance, detailed licensing management, and control over physical hardware, though at a higher cost.
- **Dedicated Instances** provide a balance by offering dedicated hardware benefits without the full control features of Dedicated Hosts, making them suitable for performance-sensitive applications that do not require detailed compliance management.