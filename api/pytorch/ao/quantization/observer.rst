torch.ao.quantization.observer
##############################

.. currentmodule:: torch.ao.quantization.observer

.. autosummary::
    :toctree: generated
    :nosignatures:
    :template: classtemplate.rst

    ObserverBase
    _ObserverBase
    MinMaxObserver
    MovingAverageMinMaxObserver
    PerChannelMinMaxObserver
    MovingAveragePerChannelMinMaxObserver
    HistogramObserver
    FixedQParamsObserver
    PlaceholderObserver
    RecordingObserver
    NoopObserver
    ReuseInputObserver
    default_debug_observer
    default_dynamic_quant_observer
    default_float_qparams_observer
    default_float_qparams_observer_4bit
    default_observer
    default_per_channel_weight_observer
    default_placeholder_observer
    default_weight_observer
    default_reuse_input_observer

.. warning::
    请使用 :attr:`quant_min` 和 :attr:`quant_max` 来指定观测者的范围。 :attr:`reduce_range` 将在未来的 PyTorch 版本中弃用。

    默认观测者 :attr:`qscheme` 只能选择以下选项之一：

    - ``torch.per_tensor_affine``
    - ``torch.per_tensor_symmetric``
    - ``torch.per_channel_affine``
    - ``torch.per_channel_symmetric``

    默认观测者 :attr:`dtype` 只能选择以下选项之一： :data:`qint8`、:data:`quint8`、:data:`quint4x2`