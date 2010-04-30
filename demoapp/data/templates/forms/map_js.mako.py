from mako import runtime, filters, cache
UNDEFINED = runtime.UNDEFINED
__M_dict_builtin = dict
__M_locals_builtin = locals
_magic_number = 5
_modified_time = 1272622938.4836731
_template_filename='/home/tsauerwein/Documents/tryz/geoalchemy_dev/geoformalchemy/demoapp/demoapp/templates/forms/map_js.mako'
_template_uri='/forms/map_js.mako'
_template_cache=cache.Cache(__name__, _modified_time)
_source_encoding='utf-8'
from webhelpers.html import escape
_exports = []


def render_body(context,**pageargs):
    context.caller_stack._push_frame()
    try:
        __M_locals = __M_dict_builtin(pageargs=pageargs)
        __M_writer = context.writer()
        # SOURCE LINE 2
        __M_writer(u'OpenLayers.Control.ModifyFeature.prototype.handleKeypress = function(evt) {\n        var code = evt.keyCode;\n        \n        // check for delete key\n        if(this.feature &&\n           !this.dragControl.handlers.drag.dragging &&\n           OpenLayers.Util.indexOf(this.deleteCodes, code) != -1) {\n            var vertex = this.dragControl.feature;\n            if(vertex &&\n               OpenLayers.Util.indexOf(this.vertices, vertex) != -1 &&\n               vertex.geometry.parent) {\n                // remove the vertex\n                vertex.geometry.parent.removeComponent(vertex.geometry);\n                this.layer.drawFeature(this.feature, this.standalone ?\n                                       undefined :\n                                       this.selectControl.renderIntent);\n                this.resetVertices();\n                this.setFeatureState();\n                this.onModification(this.feature);\n                this.layer.events.triggerEvent("featuremodified", \n                                               {feature: this.feature});\n            } else {\n                // if not pointing to a vertex, remove the whole feature\n                var feature = this.feature;\n                \n                var continueRemoving = this.layer.events.triggerEvent("beforefeatureremoved", \n                                               {feature: feature});\n                if (continueRemoving === false) {\n                    return;\n                }\n\n                this.layer.removeFeatures([feature], {silent: true});\n                feature.state = OpenLayers.State.DELETE;\n                this.layer.events.triggerEvent("featureremoved", \n                                           {feature: feature});\n                this.unselectFeature(feature);\n            }\n        }\n    };\n\nfunction init_map(\n        field_name,\n        read_only,\n        is_collection,\n        geometry_type,\n        lon,\n        lat,\n        zoom,\n        base_layer,\n        wkt\n                           ) {    \n    var map, layer, vlayer, panelControls;\n    var geometry_field = document.getElementById(field_name);\n    var wkt_parser = new OpenLayers.Format.WKT();\n    \n    layer = base_layer;\n    vlayer = new OpenLayers.Layer.Vector("Geometries");\n    \n    if (read_only) {\n        // in read-mode, only show navigation control\n        panelControls = [new OpenLayers.Control.Navigation()];\n    } else {\n        /**\n         * When the geometry of a feature changes, then the WKT string of\n         * this feature has to be written to a input field. So that\n         * when the form is submitted, the data can be read from this\n         * input field.\n         */\n        var update_geometry_field = function (feature) {\n            var wkt = null;\n            if (feature === null || \n                    ((feature instanceof Array) && (feature.length <= 0))) {\n                wkt = \'\';\n            } else {\n                wkt = wkt_parser.write(feature);\n            }\n            geometry_field.value = wkt;\n        };\n        \n        /**\n         * Creates an array containing all features of\n         * the vector layer. OpenLayers can not create \n         * WKT string from a GeometryCollection, so that\'s\n         * why we are constructing an array of Geometries.\n         */\n        var get_feature_collection = function () {\n            var collection_feature = [];\n            for (var i = 0; i < vlayer.features.length; i++) {\n                collection_feature.push(vlayer.features[i]);\n            }\n            return collection_feature;\n        };\n        \n        /**\n         * When a features is modified, update the geometry field.\n         */\n        var feature_modified_handler = function (event) {\n            var features = null;\n            if (is_collection) {\n                features = get_feature_collection();\n            } else {\n                if (event.feature.state !== OpenLayers.State.DELETE) {\n                    features = event.feature;\n                }\n            }\n            update_geometry_field(features);\n        };\n        \n        /**\n         * When a features is added, update the geometry field. If the geometry\n         * type is \'Collection\', construct an array of the already existing \n         * features and add the new feature to this array.\n         */\n        var before_feature_added_handler = function (event) {\n            if (is_collection) {\n                var collection_feature = get_feature_collection();\n                //collection_feature.push(event.feature);\n\n                update_geometry_field(collection_feature);\n\n                return true;\n            } else if (vlayer.features.length > 1) {\n                // remove old feature(s)\n                var old_features = [vlayer.features[0]];\n                vlayer.removeFeatures(old_features);\n                vlayer.destroyFeatures(old_features);\n            }\n\n            update_geometry_field(event.feature);\n\n            return true;\n        };\n        \n        vlayer.events.on({"featuremodified": feature_modified_handler});\n        vlayer.events.on({"beforefeatureadded": before_feature_added_handler});\n        vlayer.events.on({"afterfeaturemodified": feature_modified_handler});\n        \n        panelControls = [new OpenLayers.Control.Navigation()];\n        \n        if (geometry_type === \'Polygon\' || geometry_type === \'Collection\') {\n            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,\n                     OpenLayers.Handler.Polygon,\n                     {\'displayClass\': \'olControlDrawFeaturePolygon\'}));\n        }    \n\n        \n        if (geometry_type === \'Point\' || geometry_type === \'Collection\') {\n            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,\n                     OpenLayers.Handler.Point,\n                     {\'displayClass\': \'olControlDrawFeaturePoint\'}));\n        }  \n        \n\n        \n        if (geometry_type === \'Path\' || geometry_type === \'Collection\') {\n            panelControls.push(new OpenLayers.Control.DrawFeature(vlayer,\n                     OpenLayers.Handler.Path,\n                     {\'displayClass\': \'olControlDrawFeaturePath\'}));\n        }  \n        \n        var controlModifyFeature = new OpenLayers.Control.ModifyFeature(vlayer,\n                {\'displayClass\': \'olControlModifyFeature\'});\n        panelControls.push(controlModifyFeature);\n    }\n    \n    map = new OpenLayers.Map(\'map_\' + field_name);\n    \n    var toolbar = new OpenLayers.Control.Panel({\n        displayClass: \'olControlEditingToolbar\',\n        defaultControl: panelControls[0]\n    });\n    toolbar.addControls(panelControls);\n    map.addControl(toolbar);\n\n    map.addLayers([layer, vlayer]);\n\n    // try to get the geometry\n    if (wkt !== \'\') {\n        var features = wkt_parser.read(wkt);\n        if (!(features instanceof Array)) {\n            features = [features];\n        }\n        vlayer.addFeatures(features, {\'silent\': true});\n        \n        /* OpenLayers creates an array of features when the WKT string \n         * represents a GeometryCollection. To get the centroid of all\n         * features, we have to create a \'real\' GeometryCollection.\n         */\n        var geometry_collection = new OpenLayers.Geometry.Collection();\n        for (var i = 0; i < features.length; i++) {\n            geometry_collection.addComponents(features[i].geometry);\n        }\n        var centroid = geometry_collection.getCentroid();\n        \n        map.setCenter(new OpenLayers.LonLat(centroid.x, centroid.y), zoom);\n    } else {\n        map.setCenter(new OpenLayers.LonLat(lon, lat), zoom);\n    }   \n}')
        return ''
    finally:
        context.caller_stack._pop_frame()

