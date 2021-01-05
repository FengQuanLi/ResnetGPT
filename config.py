
class GPT2Config(object):
    def __init__(
            self,
            vocab_size_or_config_json_file=12491,
            n_positions=1024,
            n_ctx=512,
            n_embd=768,
            n_layer=6,
            n_head=6,
            layer_norm_epsilon=1e-5,
            initializer_range=0.02,
    ):
        self.vocab_size = vocab_size_or_config_json_file
        self.n_ctx = n_ctx
        self.n_positions = n_positions
        self.n_embd = n_embd
        self.n_layer = n_layer
        self.n_head = n_head
        self.layer_norm_epsilon = layer_norm_epsilon
        self.initializer_range = initializer_range

class TransformerConfig(object):
    def __init__(
            self,
            d_model=768,
            n_layers=12,
            heads=12,
            dropout=0.0,
            load_weights='weights'
    ):
        self.d_model = d_model
        self.n_layers = n_layers
        self.heads = heads
        self.dropout = dropout
        self.load_weights = load_weights


class GPT2Config(object):
    def __init__(
            self,
            vocab_size_or_config_json_file=12491,
            n_positions=1024,
            n_ctx=1024,
            n_embd=768,
            n_layer=12,
            n_head=12,
            layer_norm_epsilon=1e-5,
            initializer_range=0.02,
    ):
        self.vocab_size = vocab_size_or_config_json_file
        self.n_ctx = n_ctx
        self.n_positions = n_positions
        self.n_embd = n_embd
        self.n_layer = n_layer
        self.n_head = n_head
        self.layer_norm_epsilon = layer_norm_epsilon
        self.initializer_range = initializer_range